rule _Matrix_Dongle__TDi_GmbH_gzolkn
{
	meta:
		description = "Matrix Dongle __ TDi GmbH"
	strings:
		$a = {E800000000E800000000595A2BCA2BD1E81AFFFFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
