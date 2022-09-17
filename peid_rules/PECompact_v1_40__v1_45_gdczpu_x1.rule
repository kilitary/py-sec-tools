rule _PECompact_v1_40__v1_45_gdczpu
{
	meta:
		description = "PECompact v1_40 _ v1_45"
	strings:
		$a = {EB0668????????C39C60E802??????33C08BC483C004938BE38B5BFC81EB0FA040??87DD8B85A6A040??018503A040??66C785??A040??909001859EA040??BB8A11}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
