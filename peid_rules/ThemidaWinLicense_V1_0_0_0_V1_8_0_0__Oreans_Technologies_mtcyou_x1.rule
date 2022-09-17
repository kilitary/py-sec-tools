rule _ThemidaWinLicense_V1_0_0_0_V1_8_0_0__Oreans_Technologies_mtcyou
{
	meta:
		description = "ThemidaWinLicense V1_0_0_0_V1_8_0_0 __ Oreans Technologies"
	strings:
		$a = {B800000000600BC07458E8000000005805??0000008038E975??61EB??E800000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
