rule _PECompact_v1_24_2__v1_24_3_fbqhod
{
	meta:
		description = "PECompact v1_24_2 _ v1_24_3"
	strings:
		$a = {EB0668????????C39C60E802??????33C08BC483C004938BE38B5BFC81EB0F7040??87DD8B85A67040??0185037040??66C785704090??9001859E7040BB??D209}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
