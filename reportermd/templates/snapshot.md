#### {{ locality }}, {{ state }} {{ postal_code }} @{{ time }}
**Temperature**: {{ tempF }}&deg;F / Humidity: {{ humidity }} / Wind: {{ wind_direction }} {{ windMPH }} mph
**Lat / Long**: {{ lat_long }}
{% if responses %}
    {% for resp in responses %}
        {% if 'tokens' in resp %}
    **{{ resp['questionPrompt'] }}**
            {% for token in resp['tokens'] %}
        - {{ token['text'] }}
            {% endfor %}
        {% elif 'locationResponse' in resp %}
    **{{ resp['questionPrompt'] }}**
        - {{ resp['locationResponse']['text'] }}
        {% elif 'answeredOptions' in resp %}
    **{{ resp['questionPrompt'] }}**
            {% for opt in resp['answeredOptions'] %}
        - {{ opt }}
            {% endfor %}
        {% endif %}

    {% endfor %}
{% endif %}
