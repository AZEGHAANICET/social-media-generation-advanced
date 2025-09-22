


def post_prompt(count, topic, platform):
    prompt = f"""
        Generate {count} engaging post ideas about {topic} for {platform}
        For each idea, provide:
        - A catchy title (title)      
        - Key points to cover (
        - suggested Visual elements
        """
    return prompt


def hashtags_prompt(count, topic, platform, content):
    prompt = f"""
        Generate {count} relevant hashtags for this content on {platform}
        {content}
        Return only the hashtags as a comma-separated list.        
        """

def caption_prompt(platform, tone, max_length):
    prompt = f"""
        You are a professional social media content creator specializing in {platform}
        create engaging content with a {tone} tone.
        Maximum length must be : {max_length} characters
        """
