import asyncio
from plugin_manager import PluginManager

async def main():
    manager = PluginManager("plugins")
    manager.load_plugins()

    sample_text = "Bonjour la pluie est douce. The weather is good today."

    for plugin in manager.get_plugins():
        print(f"Plugin: {plugin.name} ({plugin.version})")
        print(f"-> {plugin.description}")
        print("Sync:", plugin.analyze(sample_text))
        result = await plugin.async_analyze(sample_text)
        print("Async:", result)
        print("-" * 40)

if __name__ == "__main__":
    asyncio.run(main())
