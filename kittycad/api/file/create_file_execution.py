from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.code_output import CodeOutput
from ...models.error import Error
from ...models.code_language import CodeLanguage
from ...types import Response

def _get_kwargs(
	lang: CodeLanguage,
	output: str,
	body: bytes,
	*,
	client: Client,
) -> Dict[str, Any]:
	url = "{}/file/execute/{lang}?output={output}".format(client.base_url, lang=lang, output=output)

	headers: Dict[str, Any] = client.get_headers()
	cookies: Dict[str, Any] = client.get_cookies()

	return {
		"url": url,
		"headers": headers,
		"cookies": cookies,
		"timeout": client.get_timeout(),
		"content": body,
	}


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, CodeOutput, Error]]:
	if response.status_code == 200:
		response_200 = CodeOutput.from_dict(response.json())
		return response_200
	if response.status_code == 400:
		response_4XX = Error.from_dict(response.json())
		return response_4XX
	if response.status_code == 500:
		response_5XX = Error.from_dict(response.json())
		return response_5XX
	return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, CodeOutput, Error]]:
	return Response(
		status_code=response.status_code,
		content=response.content,
		headers=response.headers,
		parsed=_parse_response(response=response),
	)


def sync_detailed(
	lang: CodeLanguage,
	output: str,
	body: bytes,
	*,
	client: Client,
) -> Response[Union[Any, CodeOutput, Error]]:
	kwargs = _get_kwargs(
		lang=lang,
		output=output,
		body=body,
		client=client,
	)

	response = httpx.post(
		verify=client.verify_ssl,
		**kwargs,
	)

	return _build_response(response=response)


def sync(
	lang: CodeLanguage,
	output: str,
	body: bytes,
	*,
	client: Client,
) -> Optional[Union[Any, CodeOutput, Error]]:

	return sync_detailed(
		lang=lang,
		output=output,
		body=body,
		client=client,
	).parsed


async def asyncio_detailed(
	lang: CodeLanguage,
	output: str,
	body: bytes,
	*,
	client: Client,
) -> Response[Union[Any, CodeOutput, Error]]:
	kwargs = _get_kwargs(
		lang=lang,
		output=output,
		body=body,
		client=client,
	)

	async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
		response = await _client.post(**kwargs)

	return _build_response(response=response)


async def asyncio(
	lang: CodeLanguage,
	output: str,
	body: bytes,
	*,
	client: Client,
) -> Optional[Union[Any, CodeOutput, Error]]:

	return (
		await asyncio_detailed(
		lang=lang,
		output=output,
		body=body,
			client=client,
		)
	).parsed
