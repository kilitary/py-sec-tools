rule _RPolyCryptor_V1_4_2__Vaska__Sign_By_fly_alqjhw
{
	meta:
		description = "RPolyCryptor V1_4_2 __ Vaska _ Sign_By_fly"
	strings:
		$a = {000000000000000000000000????????????????00000000000000000000000000000000000000006B65726E656C33322E646C6C000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
