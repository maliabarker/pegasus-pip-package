from phoenixpegasus import StellarObject, PegasusGrid

# testing instantiating object w/ position
# test_stell_obj = StellarObject(position="22h53m16.7s-14d15m49s")
# testing instantiating object w/ name
test_stell_obj = StellarObject(star_name='GJ 338 B')
print(test_stell_obj.star_name)
print(test_stell_obj.position)
# testing getting parameters
test_stell_obj.get_stellar_parameters()
print(test_stell_obj.__dict__)
# print(test_stell_obj.pm_data.__dict__)
print(test_stell_obj.fluxes.__dict__)
# testing flux processing
test_stell_obj.fluxes.convert_scale_photosphere_subtract_fluxes()
print(test_stell_obj.fluxes.__dict__)
# testing instantiating pegasus grid object
test_grid_obj = PegasusGrid(test_stell_obj)
print(test_grid_obj.stellar_obj.__dict__)
test_grid_obj.query_pegasus_subtype()
print(test_grid_obj.subtype)
models_in_limits = test_grid_obj.query_pegasus_models_in_limits()
print(models_in_limits)
print(models_in_limits[0])
fits_file_data = models_in_limits[0].get_fits_data()
print(fits_file_data)
# models_with_chi_squared = test_grid_obj.query_pegasus_chi_square()
# print(models_with_chi_squared)
# models_weighted = test_grid_obj.query_pegasus_weighted_fuv()
# print(models_weighted)
# models_flux_ratio = test_grid_obj.query_pegasus_flux_ratio()
# print(models_flux_ratio)