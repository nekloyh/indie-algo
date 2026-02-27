import torch


def solve(A: torch.Tensor, B: torch.Tensor, C: torch.Tensor, N: int):
    torch.add(A[:N], B[:N], out=C[:N])
    return C


def main():
    N = 4
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    A = torch.tensor([1.0, 2.0, 3.0, 4.0], device=device, dtype=torch.float32)
    B = torch.tensor([5.0, 6.0, 7.0, 8.0], device=device, dtype=torch.float32)

    C = torch.empty(N, device=device, dtype=torch.float32)

    result = solve(A, B, C, N)

    print(f"Result on {device}: {result}")


if __name__ == "__main__":
    main()
