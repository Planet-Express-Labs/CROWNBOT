﻿# This software is provided free of charge without a warranty.
# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was 
# this file, You can obtain one at https://mozilla.org/MPL/2.0/.

# This file servers as a library for interfacing with the models we are using with HuggingFace.
# Once OpenAI goes public or when I get a key, many of the models will be transitioned to using GPT3.
# import json
# import requests
import asyncio
import aiohttp
import json

import requests
import ujson

from CROWNBOT.config import HF_API_KEY


class Inferences:
    def __init__(self, headers=None, use_gpu=False, use_cache=True, wait_for_model=False):
        self.API_URL = None

        self.use_gpu = use_gpu
        self.use_cache = use_cache
        self.wait_for_model = wait_for_model

        if headers is None:
            # Some time down the road, it's probably worth re working how the API keys are handled.
            self.headers = {"Authorization": f"Bearer {HF_API_KEY}"}


class NLP(Inferences):

    async def direct_query(self, payload):
        """[summary]
        Args:
            payload (dict): Data to send to API.
        Returns:
            [dict]: [data returned from API]
        """

        data = json.dumps(payload)
        response = requests.request(
            "POST", self.API_URL, headers=self.headers, data=data)
        val = json.loads(response.content.decode("utf-8"))
        if "error" in val and "is currently loading" in val["error"]:
            await asyncio.sleep(2)
            return await self.direct_query(payload)
        return val


class Gpt2(NLP):
    def __init__(self):
        super().__init__()
        self.API_URL = "https://api-inference.huggingface.co/models/gpt2"

    async def expand_text(self, text):
        data = {
            "inputs": text
        }
        data = await self.direct_query(data)
        print(data)
        data = data[0]
        return data["generated_text"]


class GptNeo(NLP):
    def __init__(self):
        super().__init__()
        self.API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7B"


class BartMNLI(NLP):
    def __init__(self, API_URL=None, headers=None):
        super().__init__(headers)
        self.API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

    async def catagorize(self, inputs, labels, multi_label=False, use_gpu=False, use_cache=True, wait_for_model=False):
        """Sees how much a label applies to a given input. Coroutine. 
        Args:
            inputs (string): String to pass to BART
            labels (list): BART labels to score. 
            multi_label (bool, optional): Boolean that is set to True if classes can overlap. Defaults to False.
            use_gpu (bool, optional): If you are going to be using GPU on HuggingFace. This is only for certain plans.
             Defaults to False.
            use_cache (bool, optional): If the HuggingFace cache should be used. This should only be disabled on
             large models <10 GO. Defaults to True.
            wait_for_model (bool, optional): Defaults to False.
        Returns:
            [type]: [description]
        """
        data = await self.direct_query(
            {
                "inputs": inputs,
                "parameters": {
                    "candidate_labels": labels,
                    "multi_label": multi_label
                },
                "options": {
                    "use_gpu": use_gpu,
                    "use_cache": use_cache,
                    "wait_for_model": wait_for_model
                }
            }
        )
        try:
            return data["scores"]
        except KeyError:
            return data


class BartCnn(NLP):
    def __init__(self, API_URL=None, headers=None):
        super().__init__(headers)
        if API_URL is None:
            self.API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

    async def summarize(self, inputs: str, min_length=None, max_length=None, top_k=None, top_p=None, temperature=1.0,
                        repetition_penalty=None, max_time=None, use_gpu=False, use_cache=True, wait_for_model=False):
        data = {
            "inputs": inputs,
            "parameters": {
                "min_length": min_length,
                "max_length": max_length,
                "top_k": top_k,
                "top_p": top_p,
                "temperature": temperature,
                "repetition_penalty": repetition_penalty,
                "max_time": max_time
            },
            "options": {
                "use_gpu": use_gpu,
                "use_cache": use_cache,
                "wait_for_model": wait_for_model
            }
        }
        data = {"inputs": inputs}
        resp = await self.direct_query(data)
        try:
            resp = resp[0]
            print(resp)
            return resp["summary_text"]
        except KeyError:
            return resp


class DialoGPT(NLP):
    def __init__(self):
        super().__init__()
        self.API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"

    async def generate_response(self, input: str, past_input: list, last_responses: list, min_length=None,
                                max_length=None, top_k=None, top_p=None, temperature=1.0,
                                repetition_penalty=None, max_time=None):
        data = await self.direct_query(
            {
                "inputs": {
                    "past_user_inputs": past_input,
                    "generated_responses": last_responses,
                    "text": input
                },
                "parameters": {
                    "min_length": min_length,
                    "max_length": max_length,
                    "top_k": top_k,
                    "top_p": top_p,
                    "temperature": temperature,
                    "repetition_penalty": repetition_penalty,
                    "max_time": max_time
                },
                "options": {
                    "use_gpu": self.use_gpu,
                    "use_cache": self.use_cache,
                    "wait_for_model": self.wait_for_model
                }
            }
        )
        conv = data["conversation"]
        return data["generated_text"], conv["generated_responses"], conv["past_user_inputs"]


class distilbert(NLP):
    def __init__(self):
        super().__init__()
        self.API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

    async def classify(self, inputs):
        data = await self.direct_query({
            "inputs": inputs,
            "options": {
                "use_gpu": self.use_gpu,
                "use_cache": self.use_cache,
                "wait_for_model": self.wait_for_model
            }
        })
        return data


class Wav2Vec2(Inferences):
    def __init__(self):
        super().__init__()
        self.API_URL = "https://api-inference.huggingface.co/models/facebook/wav2vec2-base-960h"

    def convert(self, filename):
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.request("POST", self.API_URL, headers=self.headers, data=data)
        return json.loads(response.content.decode("utf-8"))["text"]
