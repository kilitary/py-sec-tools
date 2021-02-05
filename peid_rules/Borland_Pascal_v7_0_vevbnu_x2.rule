rule _Borland_Pascal_v7_0_vevbnu
{
	meta:
		description = "Borland Pascal v7_0"
	strings:
		$a = {B8????8ED88C??????8CD38CC02BD88BC405????C1????03D8B4??CD210E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
