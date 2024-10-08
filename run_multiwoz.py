import argparse

from utils import *
import engine
from evaluate import evaluate_by_domain

def run_multiwoz(model_name='gpt-3.5-turbo', dialog_id='random', domain='all', user_simulator_prompt_path=None):

    # load data
    data = load_data()
    print(f"Lenght of data: {len(data)}")

    # read user simulator prompt
    if user_simulator_prompt_path:
        with open(user_simulator_prompt_path, "r") as f:
            user_simulator_prompt = f.read()
            print(f"\n# User simulator prompt:\n{user_simulator_prompt}")
    else:
        assert False, "User simulator prompt path is required."

    # load data split
    dialog, dialog_id = pick_dialog(data, dialog_id=dialog_id, domain=domain, exclusive=False)
    print_dialog_goal(dialog, dialog_id)
    print("\n##############################################\n")

    # show ground truth dialog text
    show_dialog_text(dialog)
    print("\n##############################################\n")

    # engine
    run_result = engine.run(dialog, agent_type='react', agent_model=model_name, user_model=model_name, user_simulator_prompt=user_simulator_prompt)

    # evaluate
    for domain in DOMAINS:
        if not dialog['goal'].get(domain):
            continue
        print('=' * 40)
        try:
            eval_result = evaluate_by_domain(domain, run_result)
        except Exception as e:
            msg = f'Run dialog failed as {e.__class__.__name__}: '
            print(colored(msg, 'red') + str(e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', '-m', default='gpt-3.5-turbo')
    parser.add_argument('--dialog_id', '-i', default='random')
    parser.add_argument('--domain', '-d', default='all')
    parser.add_argument('--user_simulator_prompt_path', '-p', default='user_simulator_prompt.txt')
    args = parser.parse_args()

    run_multiwoz(model_name=args.model, dialog_id=args.dialog_id, domain=args.domain, user_simulator_prompt_path=args.user_simulator_prompt_path)

    