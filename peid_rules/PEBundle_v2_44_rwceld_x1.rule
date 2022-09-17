rule _PEBundle_v2_44_rwceld
{
	meta:
		description = "PEBundle v2_44"
	strings:
		$a = {9C60E802??????33C08BC483C004938BE38B5BFC81EB????40??87DD83BD}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
