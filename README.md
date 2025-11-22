<!-- Generator: Widdershins v4.0.1 -->

<h1 id="BlixScraper">BlixScraper</h1>

> Prosty scraper pozwalający na pobranie sklepów, gazetek i ofert z gazetek na stronie https://blix.pl/. Projekt został stworzony w formie modułu do wykorzystania w osobnej aplikacji.

## Sklepy

`GET /shops`

> Example responses

> 200 Response

```json
[
  {
    "title": "string",
    "slug": "string",
    "url": "http://example.com",
    "image": "http://example.com"
  }
]
```

<h3 id="get_shops_shops_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="get_shops_shops_get-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Shops Shops Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response Get Shops Shops Get|[[Shop](#schemashop)]|false|none|none|
|» Shop|[Shop](#schemashop)|false|none|none|
|»» title|string|true|none|none|
|»» slug|string|true|none|none|
|»» url|string(uri)|true|none|none|
|»» image|string(uri)|true|none|none|

## Gazetki

<a id="opIdget_leaflets_shops__shop__leaflets_get"></a>

`GET /shops/{shop}/leaflets`

<h3 id="get_leaflets_shops__shop__leaflets_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shop|path|string|true|slug sklepu|

> Example responses

> 200 Response

```json
[
  {
    "brand_name": "string",
    "brand_slug": "string",
    "id": "string",
    "name": "string",
    "start": "2019-08-24T14:15:22Z",
    "end": "2019-08-24T14:15:22Z",
    "url": "http://example.com",
    "image": "http://example.com"
  }
]
```

<h3 id="get_leaflets_shops__shop__leaflets_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_leaflets_shops__shop__leaflets_get-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Leaflets Shops  Shop  Leaflets Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response Get Leaflets Shops  Shop  Leaflets Get|[[LeafletPreview](#schemaleafletpreview)]|false|none|none|
|» LeafletPreview|[LeafletPreview](#schemaleafletpreview)|false|none|none|
|»» brand_name|string|true|none|none|
|»» brand_slug|string|true|none|none|
|»» id|string|true|none|none|
|»» name|string|true|none|none|
|»» start|string(date-time)|true|none|none|
|»» end|string(date-time)|true|none|none|
|»» url|string(uri)|true|none|none|
|»» image|string(uri)|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Oferty z gazetki

<a id="opIdget_leaflet_shops__shop__leaflets__leaflet__get"></a>

> Code samples

`GET /shops/{shop}/leaflets/{leaflet}`

<h3 id="get_leaflet_shops__shop__leaflets__leaflet__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shop|path|string|true|slug sklepu|
|leaflet|path|string|true|id gazetki|

> Example responses

> 200 Response

```json
[
  {
    "brand": "string",
    "start": "2019-08-24T14:15:22Z",
    "end": "2019-08-24T14:15:22Z",
    "image": "http://example.com",
    "manufacturer": "string",
    "name": "string",
    "price": 0,
    "discount": 0
  }
]
```

<h3 id="get_leaflet_shops__shop__leaflets__leaflet__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="get_leaflet_shops__shop__leaflets__leaflet__get-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Leaflet Shops  Shop  Leaflets  Leaflet  Get*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response Get Leaflet Shops  Shop  Leaflets  Leaflet  Get|[[Offer](#schemaoffer)]|false|none|none|
|» Offer|[Offer](#schemaoffer)|false|none|none|
|»» brand|string|true|none|none|
|»» start|string(date-time)|true|none|none|
|»» end|string(date-time)|true|none|none|
|»» image|string(uri)|true|none|none|
|»» manufacturer|any|true|none|none|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|string|false|none|none|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|null|false|none|none|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» name|string|true|none|none|
|»» price|any|false|none|none|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|integer|false|none|none|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|null|false|none|none|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» discount|integer|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_LeafletPreview">LeafletPreview</h2>
<!-- backwards compatibility -->
<a id="schemaleafletpreview"></a>
<a id="schema_LeafletPreview"></a>
<a id="tocSleafletpreview"></a>
<a id="tocsleafletpreview"></a>

```json
{
  "brand_name": "string",
  "brand_slug": "string",
  "id": "string",
  "name": "string",
  "start": "2019-08-24T14:15:22Z",
  "end": "2019-08-24T14:15:22Z",
  "url": "http://example.com",
  "image": "http://example.com"
}

```

LeafletPreview

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|brand_name|string|true|none|none|
|brand_slug|string|true|none|none|
|id|string|true|none|none|
|name|string|true|none|none|
|start|string(date-time)|true|none|none|
|end|string(date-time)|true|none|none|
|url|string(uri)|true|none|none|
|image|string(uri)|true|none|none|

<h2 id="tocS_Offer">Offer</h2>
<!-- backwards compatibility -->
<a id="schemaoffer"></a>
<a id="schema_Offer"></a>
<a id="tocSoffer"></a>
<a id="tocsoffer"></a>

```json
{
  "brand": "string",
  "start": "2019-08-24T14:15:22Z",
  "end": "2019-08-24T14:15:22Z",
  "image": "http://example.com",
  "manufacturer": "string",
  "name": "string",
  "price": 0,
  "discount": 0
}

```

Offer

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|brand|string|true|none|none|
|start|string(date-time)|true|none|none|
|end|string(date-time)|true|none|none|
|image|string(uri)|true|none|none|
|manufacturer|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|price|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|discount|integer|true|none|none|

<h2 id="tocS_Shop">Shop</h2>
<!-- backwards compatibility -->
<a id="schemashop"></a>
<a id="schema_Shop"></a>
<a id="tocSshop"></a>
<a id="tocsshop"></a>

```json
{
  "title": "string",
  "slug": "string",
  "url": "http://example.com",
  "image": "http://example.com"
}

```

Shop

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|string|true|none|none|
|slug|string|true|none|none|
|url|string(uri)|true|none|none|
|image|string(uri)|true|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

