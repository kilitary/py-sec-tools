rule _VIRUS__I_Worm_Hybris_nwgbfo
{
	meta:
		description = "VIRUS _ I_Worm_Hybris"
	strings:
		$a = {EB16A854????4741424C4B434743????????????524953??FC684C7040??FF15}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
