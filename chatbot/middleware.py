class ThemeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.themes = [
            {
                'header': '#a8d5e2',  # Soft Sky Blue
                'user_message': '#d4f1f4',  # Very Soft Sky Blue
                'bot_message': '#f7cac9',  # Soft Pink
                'background': '#f3e5f5',  # Soft Lavender
                'input_background': '#e8eaf6'  # Very Soft Blue
            },
            {
                'header': '#ffd1dc',  # Soft Pink
                'user_message': '#ffe5b4',  # Soft Peach
                'bot_message': '#d5f4e6',  # Soft Mint
                'background': '#fff9c4',  # Soft Yellow
                'input_background': '#e1f5fe'  # Very Soft Sky Blue
            },
            # Add more themes as needed
        ]

    def __call__(self, request):
        if 'theme_index' not in request.session:
            request.session['theme_index'] = 0
        request.session['theme'] = self.themes[request.session['theme_index']]
        request.session['theme_index'] = (request.session['theme_index'] + 1) % len(self.themes)
        response = self.get_response(request)
        return response
