rule _CubiComp_PictureMaker_graphics_format_red__jnbvqg
{
	meta:
		description = "CubiComp PictureMaker graphics format _red_"
	strings:
		$a = {160CFF0200000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
