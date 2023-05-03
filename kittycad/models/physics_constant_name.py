from enum import Enum


class PhysicsConstantName(str, Enum):
    """The valid types of phys constant names."""  # noqa: E501

    """# pi - Ratio of a circle's circumference to its diameter. <https://en.wikipedia.org/wiki/Pi> """  # noqa: E501
    PI = "pi"
    """# c - Speed of light in vacuum. <https://en.wikipedia.org/wiki//Speed_of_light> """  # noqa: E501
    C = "c"
    """# Speed of light in a vacuum. <https://en.wikipedia.org/wiki//Speed_of_light> """  # noqa: E501
    SPEED_OF_LIGHT = "speed_of_light"
    """# G - Newtonian constant of gravitation. <https://en.wikipedia.org/wiki/Gravitational_constant> """  # noqa: E501
    G = "G"
    """# Newtonian constant of gravitation. <https://en.wikipedia.org/wiki/Gravitational_constant> """  # noqa: E501
    NEWTONIAN_GRAVITATION = "newtonian_gravitation"
    """# h - Planck constant. <https://en.wikipedia.org/wiki/Planck_constant> """  # noqa: E501
    H = "h"
    """# Planck constant. <https://en.wikipedia.org/wiki/Planck_constant> """  # noqa: E501
    PLANCK_CONST = "planck_const"
    """# mu_0 - vacuum permeability. <https://en.wikipedia.org/wiki/Vacuum_permeability> """  # noqa: E501
    MU_0 = "mu_0"
    """# vacuum permeability. <https://en.wikipedia.org/wiki/Vacuum_permeability> """  # noqa: E501
    VACUUM_PERMEABILITY = "vacuum_permeability"
    """# ε_0 - vacuum permitivity. <https://en.wikipedia.org/wiki/Vacuum_permittivity> """  # noqa: E501
    E_0 = "E_0"
    """# vacuum permitivity. <https://en.wikipedia.org/wiki/Vacuum_permittivity>] """  # noqa: E501
    VACUUM_PERMITIVITY = "vacuum_permitivity"
    """# Z_0 - characteristic impedance of vacuum. <https://en.wikipedia.org/wiki/Impedance_of_free_space> """  # noqa: E501
    Z_0 = "Z_0"
    """# characteristic impedance of vacuum. <https://en.wikipedia.org/wiki/Impedance_of_free_space> """  # noqa: E501
    VACUUM_IMPEDANCE = "vacuum_impedance"
    """# k_e - Coulomb's constant. <https://en.wikipedia.org/wiki/Coulomb_constant> """  # noqa: E501
    K_E = "k_e"
    """# Coulomb's constant. <https://en.wikipedia.org/wiki/Coulomb_constant> """  # noqa: E501
    COULOMB_CONST = "coulomb_const"
    """# e - elementary charge. <https://en.wikipedia.org/wiki/Elementary_charge> """  # noqa: E501
    E = "e"
    """# elementary charge. <https://en.wikipedia.org/wiki/Elementary_charge> """  # noqa: E501
    ELEMENTARY_CHARGE = "elementary_charge"
    """# m_e - electron mass. <https://en.wikipedia.org/wiki/Electron_mass> """  # noqa: E501
    M_E = "m_e"
    """# electron mass. <https://en.wikipedia.org/wiki/Electron_mass> """  # noqa: E501
    ELECTRON_MASS = "electron_mass"
    """# m_p - proton mass. <https://en.wikipedia.org/wiki/Proton> """  # noqa: E501
    M_P = "m_p"
    """# proton mass. <https://en.wikipedia.org/wiki/Proton> """  # noqa: E501
    PROTON_MASS = "proton_mass"
    """# mu_B - Bohr magneton. <https://en.wikipedia.org/wiki/Bohr_magneton> """  # noqa: E501
    MU_B = "mu_B"
    """# Bohr magneton. <https://en.wikipedia.org/wiki/Bohr_magneton> """  # noqa: E501
    BOHR_MAGNETON = "bohr_magneton"
    """# NA - Avogadro's Number. <https://en.wikipedia.org/wiki/Avogadro_constant> """  # noqa: E501
    NA = "NA"
    """# Avogadro's Number. <https://en.wikipedia.org/wiki/Avogadro_constant> """  # noqa: E501
    AVOGADRO_NUM = "avogadro_num"
    """# R - Molar Gas constant. <https://en.wikipedia.org/wiki/Gas_constant> """  # noqa: E501
    R = "R"
    """# Molar Gas constant. <https://en.wikipedia.org/wiki/Gas_constant> """  # noqa: E501
    MOLAR_GAS_CONST = "molar_gas_const"
    """# K_B - Boltzmann constant. <https://en.wikipedia.org/wiki/Boltzmann_constant> """  # noqa: E501
    K_B = "K_B"
    """# Boltzmann constant. <https://en.wikipedia.org/wiki/Boltzmann_constant> """  # noqa: E501
    BOLTZMANN_CONST = "boltzmann_const"
    """# F - Faraday constant. <https://en.wikipedia.org/wiki/Faraday_constant> """  # noqa: E501
    F = "F"
    """# Faraday constant. <https://en.wikipedia.org/wiki/Faraday_constant> """  # noqa: E501
    FARADAY_CONST = "faraday_const"
    """# Sigma - Stefan-Boltzmann constant. <https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_constant> """  # noqa: E501
    SIGMA = "sigma"
    """# Stefan-Boltzmann constant. <https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_constant> """  # noqa: E501
    STEFAN_BOLTZMANN_CONST = "stefan_boltzmann_const"

    def __str__(self) -> str:
        return str(self.value)
