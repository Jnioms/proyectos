PROYECTO: 
Enviar alerta por telegram cuando tocan el timbre usando un optoacoplador que cierra un circuito enviando a masa un PULL-UP interno en un PIN del Sparkfun ESP32 Thing para generar el trigger del mensaje.

1) Es necesario instalar micropython en el Sparkfun ESP32 Thing. En la página oficial están las instrucciones para hacerlo: 

https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/esp32-thing

2) Yo copié el main.py usando ampy. Acá pueden encontrar los comandos que se pueden utilizar (La libreria en python que instalé usando pip es "adafruit-ampy").

https://pythonforundergradengineers.com/upload-py-files-to-esp8266-running-micropython.html

3) El PIN que estoy utilizando actualmente es el PIN 0 ya que la placa tiene un botón para probar el PULL-UP. Próximamente voy a actualizar el tutorial con la placa que uso para cerrar el circuito y enviar la señal para ejecutar el alerta.
También charlando un poco descubrí que se pueden configurar interrupciones por PIN o por tiempo. Quizas modifique el código ya que parece ser una mejor solución a la actual.

FAQs:

Es realmente necesario instalar micropython? No puede hacerse directamente en arduino?
Totalmente. Me siento cómodo programando en python y descubrí micropython y por eso lo uso. No sé como modificar el código para arduino, así que pueden utilizar el proyecto como ayuda.

Recomendás algún PIN en especial para configurar como PULL-UP?
Estuve leyendo en foros y la pagina oficial del ESP32 Thing y recomiendan usar algun pin ADC1 ya que los ADC2 dicen que funcionan en conjunto al módulo de Wifi y a veces le da prioridad al módulo y no al estado del PIN.
También los PINs desde el 34 hasta el 39 no poseen PULL-UP interno, por lo que habria que usar una resistencia externa para hacerlo.
Teniendo esas 2 cosas en cuenta, los PINs que tenía pensado usar son los 32 y 33. Pero creo que los de la otra columna pueden usarse todos tambien.

Qué es ntptime.NTP_DELTA = 3155673600+zona?
El servicio NTP envía la hora actual en la zona UTC. Para corregir la hora para mi zona (GMT-3) descubrí un truco bastante práctico que es modificar la variable NTP_DELTA que viene por default (3155673600) y restarle las horas de diferencia en segundos ("3155673600 - (-10800)" seria para GMT-3).

Para qué sirven los gc.collect()?
La memoria del ESP32 es bastante limitada y solo puede mantener abierta 1 request a https:// . Intenté usar la version http:// pero me generaba un error por no manejar correctamente la redirección a la comunicación segura. Así que intento cerrar el request por medio del telemsg2.close() pero por las dudas también ejecuto el gc.collect() para que me libere la memoria y poder enviar el siguiente mensaje.

Cómo obtengo el token y chat_id?
El token lo podés encontrar una vez generado tu bot: https://blogthinkbig.com/crear-bot-de-telegram-botfather
El chat_id lo podés encontrar con el siguiente tutorial: https://qastack.mx/programming/32423837/telegram-bot-how-to-get-a-group-chat-id#:~:text=Puede%20obtener%20ID%20de%20chat,Buscar%C3%A1s%20este%20mensaje%20m%C3%A1s%20tarde.&text=La%20solicitud%20devuelve%20una%20respuesta,de%20chat%20en%20ese%20objeto.
