# Nominator+ 📊

A comprehensive employee management system built with Python and Tkinter, designed to handle employee records, terminations, reports, and payroll management.

## 🚀 Features

- **Employee Management**: Add, remove, and manage employee records
- **Termination Processing**: Handle employee terminations with proper documentation
- **Reports Generation**: Generate various employee reports
- **Payroll Management**: Manage employee payroll information
- **Document Validation**: Validate Spanish identification documents (NIF, NIE, NAF, IBAN)

## 📋 Requirements

- Python 3.7+
- tkinter (usually comes with Python)
- sqlite3 (included with Python)
- Required image file: `Face.png` (application logo)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Nominator-plus.git
cd nominator-plus
```

2. Ensure you have Python 3.7+ installed:
```bash
python --version
```

3. Place the `Face.png` image file in the project root directory

4. Run the application:
```bash
python main.py
```

## 📁 Project Structure

```
nominator-plus/
├── main.py                 # Main application entry point
├── App.py                  # Main application GUI class
├── funcionesPy.py          # Validation utilities
├── AltasFich.py           # Employee registration module
├── BajasFic.py            # Employee termination module
├── InformesFic.py         # Reports generation module
├── NominasFich.py         # Payroll management module
├── Face.png               # Application logo
├── empleados.db           # SQLite database (auto-created)
└── README.md              # This file
```

## 🎯 Usage

### Starting the Application

Run the main application:
```bash
python main.py
```

The main window will display four main modules:

1. **ALTAS** - Employee Registration
2. **BAJAS** - Employee Termination
3. **INFORMES** - Reports
4. **NOMINAS** - Payroll

### Employee Termination (Bajas)

The termination module allows you to:
- Remove employees from the active database
- Record termination date
- Maintain termination records in a separate table

**Usage:**
1. Enter the employee code
2. Enter termination date (format: dd-mm-yyyy)
3. Click "Confirmar" to process

### Document Validation

The application includes comprehensive validation for Spanish identification documents:

- **NIF (Número de Identificación Fiscal)**: Spanish national ID
- **NIE (Número de Identidad de Extranjero)**: Foreign resident ID
- **NAF (Número de Afiliación Fiscal)**: Tax affiliation number
- **IBAN**: International Bank Account Number

## 🗄️ Database Schema

The application uses SQLite with the following tables:

### employees table
- `id`: Primary key
- `nombre`: Employee name
- `nif`: National identification
- `genero`: Gender
- Additional fields as defined in AltasFich.py

### bajas table (terminations)
- `id`: Employee ID
- `nombre`: Employee name
- `nif`: National identification
- `fecha_baja`: Termination date
- `genero`: Gender

## 🔧 Configuration

### GUI Configuration
- Window size: 500x500 pixels
- Non-resizable main window
- Grid-based layout with responsive columns

### Database Configuration
- Database file: `empleados.db`
- Auto-created on first run
- Tables created automatically if they don't exist

## 🎨 Customization

### Styling
The application uses a consistent yellow color scheme (`#FFFF99`) for buttons. You can modify the styling in the `crearApp()` method in `App.py`.

### Adding New Modules
To add new functionality:
1. Create a new Python file (e.g., `NewModule.py`)
2. Import it in `App.py`
3. Add a new button in the `crearApp()` method
4. Create a launch method following the existing pattern

## 🐛 Error Handling

The application includes error handling for:
- Missing image files
- Database connection issues
- Invalid date formats
- Document validation errors

## 📝 Validation Rules

### Date Format
- Format: dd-mm-yyyy
- Regex pattern: `^\d{2}-\d{2}-\d{4}$`

### NIF Validation
- Format: 8 digits + 1 letter
- Checksum validation using official algorithm

### NIE Validation
- Format: [XYZ] + 7 digits + 1 letter
- Checksum validation with letter substitution

### NAF Validation
- Format: A/B/C (slash-separated numbers)
- Modulo 97 validation

### IBAN Validation
- 24-character Spanish IBAN
- MOD-97 algorithm validation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 👥 Authors

- Salah Eddine Khouadri - Initial work - [MyGithub](https://github.com/5alvh)

## 🙏 Acknowledgments

- Built with Python's tkinter for cross-platform GUI support
- Uses SQLite for lightweight database management
- Implements Spanish document validation standards

## 🔮 Future Enhancements

- [ ] Add employee photo management
- [ ] Implement backup/restore functionality
- [ ] Add export to Excel/PDF features
- [ ] Implement user authentication
- [ ] Add advanced search and filtering
- [ ] Multi-language support

---

For more information or support, please open an issue on GitHub.
