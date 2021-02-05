rule _PEBundle_v0_2__v2_0x_rwkzkp
{
	meta:
		description = "PEBundle v0_2 _ v2_0x"
	strings:
		$a = {9C60E802??????33C08BC483C004938BE38B5BFC81EB????40??87DD6A0468??10????68??02????6A??FF95}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
