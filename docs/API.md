# 이미지 처리 API V0.1.0

## 개요
* 본 서는 이미지 처리 API 이다.
* API는 http 프로토콜을 사용하며 JSON 형식으로 GET, POST 방식을 사용한다. 때문에, JSON 포맷을 사용할 수 있다고 가정한다.
* 본 서비스는 이미지를 처리하기 위해 본 서비스에 이미지를 업로드하고 처리된 이미지를 다운로드 받는다.

## 용어

## API 스펙
1. host
* 개발 단계로 호스트는 로컬에서 진행한다.

2. 얼굴 모자이크
* 사진에서 얼굴을 찾아 모자이크를 해주는 기능이다.

[request]
  - path: /v1/tools/request/mosaic
  - method: POST
  - header:
    * Content-type: application/json
  - client timeout
    * 100 초
  - parameter

| 필드 | 타입 | 필수 | 설명 | 예제 |
| --- | --- | --- | --- | --- |
| test | test | test | test | test|

[response]

| 필드 | 타입 | 필수 | 설명 | 예제 |
| --- | --- | --- | --- | --- |
| test | test | test | test | test|

## 코드 정의

### 오류 코드

| Code | 설명 |
| --- | --- |
| 0000 | 정상 코드 |
| 9999 | 시스템 오류 코드 |

<br>
<hr>
<br>

# treat image API V0.1.0

## Overview
* This paper is to use treat image API. 
* This API adopts http protocol and use JSON format to GET, POST method. So, be required to be able to JSON format.
* This services is that Upload a image to process on this web services, and download processed a image.

## Terminology

## API spec
1. host
* In development, localhost is used.

2. Face mosiac
* Mosaic the area of face on a image.

[request]
  - path: /v1/tools/request/mosaic
  - method: POST
  - header:
    * Content-type: application/json
  - client timeout
    * 100 s
  - parameter

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| test | test | test | test | test|

[response]

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| test | test | test | test | test|

## Code

### Error code

| Code | Description |
| --- | --- |
| 0000 | Sucess code |
| 9999 | System error code |
