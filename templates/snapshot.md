#### {{ locality }}, {{ state }} {{ postal_code }} @{{ time }}
**Temperature**: {{ tempF }}&deg;F / Humidity: {{ humidity }} / Wind: {{ wind_direction }} {{ windMPH }} mph
**Lat / Long**: {{ lat_long }}

{% for resp in responses %}
{{ resp['questionPrompt'] }}
    {% if 'tokens' in resp %}
        {% for token in resp['tokens'] %}
    - {{ token['text'] }}
        {% endfor %}
    {% elif 'locationResponse' in resp %}
    - {{ resp['locationResponse']['text'] }}
    {% elif 'answeredOptions' in resp %}
        {% for opt in resp['answeredOptions'] %}
    - {{ opt }}
        {% endfor %}
    {% endif %}

{% endfor %}
