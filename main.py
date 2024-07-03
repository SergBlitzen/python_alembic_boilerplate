import os
import logging
import asyncio


if __name__ == "__main__":
    if not os.path.exists("logs"):
        os.mkdir("logs")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(filename)s - %(message)s",
        filename="logs/app.log"
    )

    loop = asyncio.new_event_loop()

    # Startup logic here

    loop.run_forever()
