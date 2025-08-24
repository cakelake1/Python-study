current_state = ''
history = []
current_index = -1

def BastShoe(command):
    global current_state, history, current_index
    if current_index == -1:
        history = []
        current_index = -1
        current_state = ''
    space_parts = command.split(' ', 1)
    operator_code = space_parts[0]
    parameter = space_parts[1] if len(space_parts) > 1 else ''
    if operator_code not in {'1', '2', '3', '4', '5'}:
        return current_state
    match operator_code:
        case '1':
            if current_index < len(history) - 1:
                history = [history[current_index]]
                current_index = 0
            current_state += parameter
            history.append(current_state)
            current_index = len(history) - 1
            return current_state
        case '2':
            try:
                n = int(parameter)
            except ValueError:
                return current_state
            if current_index < len(history) - 1:
                history = [history[current_index]]
                current_index = 0
            current_state = current_state[:max(0, len(current_state) - n)]
            history.append(current_state)
            current_index = len(history) - 1
            return current_state
        case '3':
            try:
                i = int(parameter)
            except ValueError:
                return ''
            if 0 <= i < len(current_state):
                return current_state[i]
            return ''
        case '4':
            if current_index > 0:
                current_index -= 1
                current_state = history[current_index]
            return current_state
        case '5':
            if current_index < len(history) - 1:
                current_index += 1
                current_state = history[current_index]
            return current_state