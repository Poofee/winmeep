# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _mpb
else:
    import _mpb

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import meep
TWOPI = _mpb.TWOPI

def map_data(d_in_re, d_in_im, n_in, d_out_re, d_out_im, n_out, coord_map, kvector, pick_nearest, verbose, multiply_bloch_phase):
    return _mpb.map_data(d_in_re, d_in_im, n_in, d_out_re, d_out_im, n_out, coord_map, kvector, pick_nearest, verbose, multiply_bloch_phase)

def with_hermitian_epsilon():
    return _mpb.with_hermitian_epsilon()
class mode_solver(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    MAX_NWORK = _mpb.mode_solver_MAX_NWORK
    epsilon_CURFIELD_TYPE = _mpb.mode_solver_epsilon_CURFIELD_TYPE
    mu_CURFIELD_TYPE = _mpb.mode_solver_mu_CURFIELD_TYPE
    NUM_FFT_BANDS = _mpb.mode_solver_NUM_FFT_BANDS
    num_bands = property(_mpb.mode_solver_num_bands_get, _mpb.mode_solver_num_bands_set)
    resolution = property(_mpb.mode_solver_resolution_get, _mpb.mode_solver_resolution_set)
    target_freq = property(_mpb.mode_solver_target_freq_get, _mpb.mode_solver_target_freq_set)
    tolerance = property(_mpb.mode_solver_tolerance_get, _mpb.mode_solver_tolerance_set)
    mesh_size = property(_mpb.mode_solver_mesh_size_get, _mpb.mode_solver_mesh_size_set)
    negative_epsilon_ok = property(_mpb.mode_solver_negative_epsilon_ok_get, _mpb.mode_solver_negative_epsilon_ok_set)
    epsilon_input_file = property(_mpb.mode_solver_epsilon_input_file_get, _mpb.mode_solver_epsilon_input_file_set)
    mu_input_file = property(_mpb.mode_solver_mu_input_file_get, _mpb.mode_solver_mu_input_file_set)
    force_mu = property(_mpb.mode_solver_force_mu_get, _mpb.mode_solver_force_mu_set)
    use_simple_preconditioner = property(_mpb.mode_solver_use_simple_preconditioner_get, _mpb.mode_solver_use_simple_preconditioner_set)
    grid_size = property(_mpb.mode_solver_grid_size_get, _mpb.mode_solver_grid_size_set)
    n = property(_mpb.mode_solver_n_get, _mpb.mode_solver_n_set)
    local_N = property(_mpb.mode_solver_local_N_get, _mpb.mode_solver_local_N_set)
    N_start = property(_mpb.mode_solver_N_start_get, _mpb.mode_solver_N_start_set)
    alloc_N = property(_mpb.mode_solver_alloc_N_get, _mpb.mode_solver_alloc_N_set)
    nwork_alloc = property(_mpb.mode_solver_nwork_alloc_get, _mpb.mode_solver_nwork_alloc_set)
    eigensolver_nwork = property(_mpb.mode_solver_eigensolver_nwork_get, _mpb.mode_solver_eigensolver_nwork_set)
    eigensolver_block_size = property(_mpb.mode_solver_eigensolver_block_size_get, _mpb.mode_solver_eigensolver_block_size_set)
    last_parity = property(_mpb.mode_solver_last_parity_get, _mpb.mode_solver_last_parity_set)
    iterations = property(_mpb.mode_solver_iterations_get, _mpb.mode_solver_iterations_set)
    eigensolver_flops = property(_mpb.mode_solver_eigensolver_flops_get, _mpb.mode_solver_eigensolver_flops_set)
    geometry_list = property(_mpb.mode_solver_geometry_list_get, _mpb.mode_solver_geometry_list_set)
    geometry_tree = property(_mpb.mode_solver_geometry_tree_get, _mpb.mode_solver_geometry_tree_set)
    vol = property(_mpb.mode_solver_vol_get, _mpb.mode_solver_vol_set)
    R = property(_mpb.mode_solver_R_get, _mpb.mode_solver_R_set)
    G = property(_mpb.mode_solver_G_get, _mpb.mode_solver_G_set)
    mdata = property(_mpb.mode_solver_mdata_get, _mpb.mode_solver_mdata_set)
    mtdata = property(_mpb.mode_solver_mtdata_get, _mpb.mode_solver_mtdata_set)
    curfield_band = property(_mpb.mode_solver_curfield_band_get, _mpb.mode_solver_curfield_band_set)
    cur_kvector = property(_mpb.mode_solver_cur_kvector_get, _mpb.mode_solver_cur_kvector_set)
    Rm = property(_mpb.mode_solver_Rm_get, _mpb.mode_solver_Rm_set)
    Gm = property(_mpb.mode_solver_Gm_get, _mpb.mode_solver_Gm_set)
    H = property(_mpb.mode_solver_H_get, _mpb.mode_solver_H_set)
    Hblock = property(_mpb.mode_solver_Hblock_get, _mpb.mode_solver_Hblock_set)
    muinvH = property(_mpb.mode_solver_muinvH_get, _mpb.mode_solver_muinvH_set)
    W = property(_mpb.mode_solver_W_get, _mpb.mode_solver_W_set)
    freqs = property(_mpb.mode_solver_freqs_get, _mpb.mode_solver_freqs_set)
    verbose = property(_mpb.mode_solver_verbose_get, _mpb.mode_solver_verbose_set)
    deterministic = property(_mpb.mode_solver_deterministic_get, _mpb.mode_solver_deterministic_set)

    def __init__(self, num_bands, resolution, lat, tolerance, mesh_size, _default_material, deterministic, target_freq, dims, verbose, periodicity, flops, negative_epsilon_ok, epsilon_input_file, mu_input_file, force_mu, use_simple_preconditioner, grid_size, eigensolver_nwork, eigensolver_block_size):
        _mpb.mode_solver_swiginit(self, _mpb.new_mode_solver(num_bands, resolution, lat, tolerance, mesh_size, _default_material, deterministic, target_freq, dims, verbose, periodicity, flops, negative_epsilon_ok, epsilon_input_file, mu_input_file, force_mu, use_simple_preconditioner, grid_size, eigensolver_nwork, eigensolver_block_size))
    __swig_destroy__ = _mpb.delete_mode_solver

    def init(self, p, reset_fields, geometry, _default_material):
        return _mpb.mode_solver_init(self, p, reset_fields, geometry, _default_material)

    def solve_kpoint(self, kpoint):
        return _mpb.mode_solver_solve_kpoint(self, kpoint)

    def using_mu(self):
        return _mpb.mode_solver_using_mu(self)

    def set_parity(self, p):
        return _mpb.mode_solver_set_parity(self, p)

    def set_num_bands(self, nb):
        return _mpb.mode_solver_set_num_bands(self, nb)

    def get_kpoint_index(self):
        return _mpb.mode_solver_get_kpoint_index(self)

    def set_kpoint_index(self, i):
        return _mpb.mode_solver_set_kpoint_index(self, i)

    def get_epsilon(self):
        return _mpb.mode_solver_get_epsilon(self)

    def get_mu(self):
        return _mpb.mode_solver_get_mu(self)

    def get_epsilon_tensor(self, c1, c2, imag, inv):
        return _mpb.mode_solver_get_epsilon_tensor(self, c1, c2, imag, inv)

    def get_material_pt(self, material, p):
        return _mpb.mode_solver_get_material_pt(self, material, p)

    def material_epsmu(self, material, epsmu, epsmu_inv, eps=True):
        return _mpb.mode_solver_material_epsmu(self, material, epsmu, epsmu_inv, eps)

    def mean_epsilon(self, meps, meps_inv, n, d1, d2, d3, tol, r):
        return _mpb.mode_solver_mean_epsilon(self, meps, meps_inv, n, d1, d2, d3, tol, r)

    def randomize_fields(self):
        return _mpb.mode_solver_randomize_fields(self)

    def init_epsilon(self, geometry_in):
        return _mpb.mode_solver_init_epsilon(self, geometry_in)

    def reset_epsilon(self, geometry):
        return _mpb.mode_solver_reset_epsilon(self, geometry)

    def has_mu(self, geometry):
        return _mpb.mode_solver_has_mu(self, geometry)

    def material_has_mu(self, mt):
        return _mpb.mode_solver_material_has_mu(self, mt)

    def curfield_reset(self):
        return _mpb.mode_solver_curfield_reset(self)

    def get_field_size(self):
        return _mpb.mode_solver_get_field_size(self)

    def get_freqs(self):
        return _mpb.mode_solver_get_freqs(self)

    def get_eigensolver_flops(self):
        return _mpb.mode_solver_get_eigensolver_flops(self)

    def get_iterations(self):
        return _mpb.mode_solver_get_iterations(self)

    def get_efield(self, band):
        return _mpb.mode_solver_get_efield(self, band)

    def get_dfield(self, band):
        return _mpb.mode_solver_get_dfield(self, band)

    def get_hfield(self, band):
        return _mpb.mode_solver_get_hfield(self, band)

    def get_bfield(self, band):
        return _mpb.mode_solver_get_bfield(self, band)

    def get_efield_from_dfield(self):
        return _mpb.mode_solver_get_efield_from_dfield(self)

    def get_curfield(self, data):
        return _mpb.mode_solver_get_curfield(self, data)

    def get_curfield_cmplx(self, cdata):
        return _mpb.mode_solver_get_curfield_cmplx(self, cdata)

    def set_curfield(self, data):
        return _mpb.mode_solver_set_curfield(self, data)

    def set_curfield_cmplx(self, cdata):
        return _mpb.mode_solver_set_curfield_cmplx(self, cdata)

    def get_lattice(self, data):
        return _mpb.mode_solver_get_lattice(self, data)

    def get_eigenvectors(self, p_start, p, cdata):
        return _mpb.mode_solver_get_eigenvectors(self, p_start, p, cdata)

    def get_eigenvectors_slice_dims(self, num_bands):
        return _mpb.mode_solver_get_eigenvectors_slice_dims(self, num_bands)

    def set_eigenvectors(self, b_start, cdata):
        return _mpb.mode_solver_set_eigenvectors(self, b_start, cdata)

    def compute_field_energy(self):
        return _mpb.mode_solver_compute_field_energy(self)

    def compute_energy_in_objects(self, objects):
        return _mpb.mode_solver_compute_energy_in_objects(self, objects)

    def get_curfield_type(self):
        return _mpb.mode_solver_get_curfield_type(self)

    def set_curfield_type(self, t):
        return _mpb.mode_solver_set_curfield_type(self, t)

    def get_parity_string(self):
        return _mpb.mode_solver_get_parity_string(self)

    def get_dims(self):
        return _mpb.mode_solver_get_dims(self)

    def set_grid_size(self, gs):
        return _mpb.mode_solver_set_grid_size(self, gs)

    def get_libctl_dimensions(self):
        return _mpb.mode_solver_get_libctl_dimensions(self)

    def set_libctl_dimensions(self, val):
        return _mpb.mode_solver_set_libctl_dimensions(self, val)

    def get_libctl_ensure_periodicity(self):
        return _mpb.mode_solver_get_libctl_ensure_periodicity(self)

    def set_libctl_ensure_periodicity(self, val):
        return _mpb.mode_solver_set_libctl_ensure_periodicity(self, val)

    def set_libctl_geometry_lattice(self, val):
        return _mpb.mode_solver_set_libctl_geometry_lattice(self, val)

    def get_output_k(self):
        return _mpb.mode_solver_get_output_k(self)

    def get_val(self, ix, iy, iz, nx, ny, nz, last_dim_size, data, stride, conjugate):
        return _mpb.mode_solver_get_val(self, ix, iy, iz, nx, ny, nz, last_dim_size, data, stride, conjugate)

    def interp_val(self, p, nx, ny, nz, last_dim_size, data, stride, conjugate):
        return _mpb.mode_solver_interp_val(self, p, nx, ny, nz, last_dim_size, data, stride, conjugate)

    def interp_cval(self, p, nx, ny, nz, last_dim_size, data, stride):
        return _mpb.mode_solver_interp_cval(self, p, nx, ny, nz, last_dim_size, data, stride)

    def interp_eps_inv(self, p):
        return _mpb.mode_solver_interp_eps_inv(self, p)

    def get_epsilon_point(self, p):
        return _mpb.mode_solver_get_epsilon_point(self, p)

    def get_epsilon_inverse_tensor_point(self, p):
        return _mpb.mode_solver_get_epsilon_inverse_tensor_point(self, p)

    def get_energy_point(self, p):
        return _mpb.mode_solver_get_energy_point(self, p)

    def get_field_point(self, p):
        return _mpb.mode_solver_get_field_point(self, p)

    def get_bloch_field_point_(self, field, p):
        return _mpb.mode_solver_get_bloch_field_point_(self, field, p)

    def get_bloch_field_point(self, p):
        return _mpb.mode_solver_get_bloch_field_point(self, p)

    def multiply_bloch_phase(self, cdata=None):
        return _mpb.mode_solver_multiply_bloch_phase(self, cdata)

    def fix_field_phase(self):
        return _mpb.mode_solver_fix_field_phase(self)

    def compute_field_divergence(self):
        return _mpb.mode_solver_compute_field_divergence(self)

    def compute_zparities(self):
        return _mpb.mode_solver_compute_zparities(self)

    def compute_yparities(self):
        return _mpb.mode_solver_compute_yparities(self)

    def compute_group_velocity_component(self, d):
        return _mpb.mode_solver_compute_group_velocity_component(self, d)

    def compute_1_group_velocity_component(self, d, b):
        return _mpb.mode_solver_compute_1_group_velocity_component(self, d, b)

    def compute_1_group_velocity(self, b):
        return _mpb.mode_solver_compute_1_group_velocity(self, b)

    def compute_1_group_velocity_reciprocal(self, b):
        return _mpb.mode_solver_compute_1_group_velocity_reciprocal(self, b)

    def compute_energy_in_dielectric(self, eps_low, eps_high):
        return _mpb.mode_solver_compute_energy_in_dielectric(self, eps_low, eps_high)

    def compute_field_integral(self, field_func):
        return _mpb.mode_solver_compute_field_integral(self, field_func)

    def compute_energy_integral(self, field_func):
        return _mpb.mode_solver_compute_energy_integral(self, field_func)

    def get_dominant_planewave(self, band):
        return _mpb.mode_solver_get_dominant_planewave(self, band)

    def transformed_overlap(self, W, w):
        return _mpb.mode_solver_transformed_overlap(self, W, w)

    def compute_symmetry(self, which_band, W, w):
        return _mpb.mode_solver_compute_symmetry(self, which_band, W, w)

# Register mode_solver in _mpb:
_mpb.mode_solver_swigregister(mode_solver)
cvar = _mpb.cvar


__version__ = (_mpb.cvar.MPB_VERSION_MAJOR, _mpb.cvar.MPB_VERSION_MINOR, _mpb.cvar.MPB_VERSION_PATCH)

from meep.verbosity_mgr import Verbosity
verbosity = Verbosity(_mpb.cvar, 'mpb', 1)

from .solver import (
    MPBArray,
    ModeSolver,
    output_hfield,
    output_hfield_x,
    output_hfield_y,
    output_hfield_z,
    output_bfield,
    output_bfield_x,
    output_bfield_y,
    output_bfield_z,
    output_dfield,
    output_dfield_x,
    output_dfield_y,
    output_dfield_z,
    output_efield,
    output_efield_x,
    output_efield_y,
    output_efield_z,
    output_charge_density,
    output_bpwr,
    output_dpwr,
    output_tot_pwr,
    output_dpwr_in_objects,
    output_poynting,
    output_poynting_x,
    output_poynting_y,
    output_poynting_z,
    output_at_kpoint,
    display_group_velocities,
    display_yparities,
    display_zparities,
    fix_hfield_phase,
    fix_bfield_phase,
    fix_dfield_phase,
    fix_efield_phase,
)

from .mpb_data import (
    MPBData,
)



MPB_VERSION_MAJOR = cvar.MPB_VERSION_MAJOR
MPB_VERSION_MINOR = cvar.MPB_VERSION_MINOR
MPB_VERSION_PATCH = cvar.MPB_VERSION_PATCH

