import torch


def save_model(model, filepath):
    """
    Save the model to the specified file path.

    Args:
        model (torch.nn.Module): The PyTorch model to save.
        filepath (str): The file path where the model will be saved.
    """
    filepath = r'C:\Users\karth\PycharmProjects\Epitome Prj\Models'
    torch.save(model.state_dict(), filepath)
    print(f"Model saved successfully to {filepath}")
