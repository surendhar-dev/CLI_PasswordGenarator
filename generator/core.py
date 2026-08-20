import secrets
import string

def generate_password(length: int, use_upper: bool, use_lower: bool, use_nums: bool, use_syms: bool) -> str:
    """Generates a random password ensuring at least one character from each selected set is included."""
    pools = []
    guaranteed_chars = []

    if use_upper:
        pools.append(string.ascii_uppercase)
        guaranteed_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        pools.append(string.ascii_lowercase)
        guaranteed_chars.append(secrets.choice(string.ascii_lowercase))
    if use_nums:
        pools.append(string.digits)
        guaranteed_chars.append(secrets.choice(string.digits))
    if use_syms:
        pools.append(string.punctuation)
        guaranteed_chars.append(secrets.choice(string.punctuation))

    if not pools:
        raise ValueError("At least one character set must be selected.")

    if length < len(guaranteed_chars):
        raise ValueError(f"Password length must be at least {len(guaranteed_chars)} to include all selected types.")

    all_chars = "".join(pools)
    remaining_length = length - len(guaranteed_chars)
    random_chars = [secrets.choice(all_chars) for _ in range(remaining_length)]

    # Combine guaranteed characters with remaining random picks and shuffle
    password_list = guaranteed_chars + random_chars
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)


def evaluate_strength(password: str) -> tuple[int, str, str]:
    """Evaluates password strength based on criteria and returns (score, rating, progress_bar)."""
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    # Map score to textual rating
    if score <= 2:
        rating = "WEAK"
        bar = "███░░░░░░░"
    elif score <= 4:
        rating = "MEDIUM"
        bar = "██████░░░░"
    elif score == 5:
        rating = "STRONG"
        bar = "████████░░"
    else:
        rating = "VERY STRONG"
        bar = "██████████"

    return score, rating, bar