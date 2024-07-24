# Inventory_Management

This project helps manage a computer store's inventory by identifying laptops priced over $1000. It uses Python and MySQL for database interaction.

## Project Structure

- `data/`: Contains sample data for testing.
- `scripts/`: Contains the main scripts for database interaction and inventory management.
- `tests/`: Contains test scripts for verifying functionality.
- `config/`: Contains configuration files.
- `requirements.txt`: Lists project dependencies.

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Configure database settings in `config/config.ini`.

3. Run the main script:
    ```bash
    python scripts/inventory_management.py
    ```

4. Run tests:
    ```bash
    python -m unittest discover -s tests
    ```

## License

This project is licensed under the MIT License.
