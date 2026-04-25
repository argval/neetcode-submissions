class TextProcessor:
    def format_text(self, *args: str) -> str:
        # Check if there is exactly one argument
        if len(args) == 1:
            return args[0].upper()
        
        # If there are multiple arguments, join them with a space
        else:
            return "".join(args)

# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
