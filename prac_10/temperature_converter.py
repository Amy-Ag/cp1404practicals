from flask import Flask

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

@app.route("/f/<celsius>")
def convert(celsius):
    """Displays fahrenheit output on the website."""
    try:
        celsius = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return f"{fahrenheit:.2f}"
    except ValueError:
        return "Invalid input."

if __name__ == '__main__':
    app.run()