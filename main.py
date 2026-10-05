import asyncio
import logging
from discord_webhook import DiscordWebhook, DiscordEmbed
from pystyle import Colors, Colorate, Write, Center

logging.getLogger("discord_webhook").setLevel(logging.CRITICAL)

async def mssg():
    print(Center.XCenter(Colorate.Horizontal(
        Colors.green_to_cyan,"╭─ WEBHOOK ─╮"
    )))

    wk = Write.Input("╰─➤ Webhook: ",Colors.green_to_cyan)
    msg = Write.Input("╰─➤ Mensaje: ",Colors.green_to_cyan)
    cn = int(Write.Input("╰─➤ Cantidad: ",Colors.green_to_cyan))

    tasks = []
    i = 0

    while True:
        if i >= cn:
            break

        print(f"\r{Colorate.Horizontal(
            Colors.green_to_cyan,
            f"Enviando [{i+1}/{cn}]"
        )}",end="")

        async def send():
            for intento in range(5):
                try:
                    webhook = DiscordWebhook(
                        url=wk,
                        content=msg
                    )

                    response = await asyncio.to_thread(
                        webhook.execute
                    )

                    if response.status_code == 204:
                        return True

                    if response.status_code == 429:
                        espera = float(
                            response.headers.get("Retry-After",2)
                        )
                    else:
                        espera = 2 ** intento

                    if intento < 4:
                        await asyncio.sleep(espera)

                except Exception:
                    if intento < 4:
                        espera = 2 ** intento

                        print(f"\r{Colorate.Horizontal(
                            Colors.yellow_to_red,
                            f"↻ Reintentando [{intento+2}/5] | espera: {espera}s"
                        )}",end="")

                        await asyncio.sleep(espera)

            return False

        tasks.append(send())
        i += 1

    resultados = await asyncio.gather(*tasks)

    print(Colorate.Horizontal(
        Colors.green_to_cyan,
        f"\n✓ Listo | Fallos: {resultados.count(False)}"
    ))


async def embd():
    wk = Write.Input("╰─➤ Webhook: ",Colors.purple_to_blue)
    msg = Write.Input("╰─➤ Mensaje: ",Colors.purple_to_blue)
    tit = Write.Input("╰─➤ Title: ",Colors.purple_to_blue)
    cn = int(Write.Input("╰─➤ Cantidad: ",Colors.purple_to_blue))

    tasks = []
    i = 0

    while True:
        if i >= cn:
            break

        print(f"\r{Colorate.Horizontal(
            Colors.purple_to_blue,
            f"Enviando [{i+1}/{cn}]"
        )}",end="")

        async def send():
            for intento in range(5):
                try:
                    webhook = DiscordWebhook(
                        url=wk,
                        content=msg
                    )

                    embed = DiscordEmbed(
                        title=tit,
                        color="720097"
                    )

                    embed.set_image(
                        url = "https://cdn.discordapp.com/attachments/1047262185438588928/1488779374848381039/ezgif-7-2aae1a2563.gif?ex=6ab218d7&is=6ab0c757&hm=7fba3ba77808715c7b559b25a4d7fb63b25aa18fd9a5a2d1a884d4b1a035a462&"
                    )

                    webhook.add_embed(embed)

                    response = await asyncio.to_thread(
                        webhook.execute
                    )

                    if response.status_code == 204:
                        return True

                    if response.status_code == 429:
                        espera = float(
                            response.headers.get("Retry-After",2)
                        )
                    else:
                        espera = 2 ** intento

                    if intento < 4:
                        await asyncio.sleep(espera)

                except Exception:
                    if intento < 4:
                        espera = 2 ** intento

                        print(f"\r{Colorate.Horizontal(
                            Colors.yellow_to_red,
                            f"↻ Reintentando [{intento+2}/5] | espera: {espera}s"
                        )}",end="")

                        await asyncio.sleep(espera)

            return False

        tasks.append(send())
        i += 1

    resultados = await asyncio.gather(*tasks)

    print(Colorate.Horizontal(
        Colors.purple_to_blue,
        f"\n✓ Listo | Fallos: {resultados.count(False)}"
    ))


async def multispm():
    print(Center.XCenter(Colorate.Horizontal(
        Colors.blue_to_cyan,
        "╭─ MULTI WEBHOOK ─╮"
    )))

    wk = Write.Input(
        "╰─➤ Archivo: ",
        Colors.blue_to_cyan
    )

    msg = Write.Input(
        "╰─➤ Mensaje: ",
        Colors.blue_to_cyan
    )

    with open(wk,"r") as file:
        webhooks = [
            x.strip()
            for x in file
            if x.strip()
        ]

    tasks = []
    i = 0

    while True:
        if i >= len(webhooks):
            break

        webhook_url = webhooks[i]

        async def send(url=webhook_url):
            for inten in range(10):
                try:
                    webhook = DiscordWebhook(
                        url=url,
                        content=msg
                    )

                    response = await asyncio.to_thread(
                        webhook.execute
                    )

                    if response.status_code == 204:
                        return True

                    if response.status_code == 429:
                        espera = float(
                            response.headers.get("Retry-After",2)
                        )
                    else:
                        espera = 2 ** intento

                    if intento < 4:
                        await asyncio.sleep(espera)

                except Exception:
                    if intento < 4:
                        espera = 2 ** intento

                        print(f"\r{Colorate.Horizontal(
                            Colors.yellow_to_red,
                            f"↻ Reintentando [{intento+2}/5] | espera: {espera}s"
                        )}",end="")

                        await asyncio.sleep(espera)

            return False

        tasks.append(send())
        i += 1

    resultados = await asyncio.gather(*tasks)

    print(Colorate.Horizontal(
        Colors.blue_to_cyan,
        f"\n✓ Enviados: {len(webhooks)} | Fallos: {resultados.count(False)}"
    ))


def main():
    while True:
        print(Colorate.Horizontal(
            Colors.purple_to_blue,
            """
       † GALAXY WEBHOOK TOOL †
    ─────────────────────────────
       [1] Enviar mensaje
       [2] Enviar embed
       [3] Multi Spam
       [4] Salir
    ─────────────────────────────
"""
        ))

        try:
            option = int(
                Write.Input(
                    "       ╰─➤ ",
                    Colors.purple_to_blue
                )
            )

            if option == 1:
                asyncio.run(mssg())

            elif option == 2:
                asyncio.run(embd())

            elif option == 3:
                asyncio.run(multispm())

            elif option == 4:
                print(Colorate.Horizontal(
                    Colors.purple_to_blue,
                    "\n† Hasta luego †"
                ))
                break

            else:
                print(Colorate.Horizontal(
                    Colors.red_to_purple,
                    "\n✗ Opción inválida"
                ))

        except ValueError:
            print(Colorate.Horizontal(
                Colors.red_to_purple,
                "\n✗ Introduce un número"
            ))

        except FileNotFoundError:
            print(Colorate.Horizontal(
                Colors.red_to_purple,
                "\n✗ Archivo no encontrado"
            ))

        except KeyboardInterrupt:
            print("\n")


if __name__ == "__main__":
    main()
