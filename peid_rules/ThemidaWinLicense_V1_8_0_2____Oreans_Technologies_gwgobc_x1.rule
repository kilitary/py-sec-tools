rule _ThemidaWinLicense_V1_8_0_2____Oreans_Technologies_gwgobc
{
	meta:
		description = "ThemidaWinLicense V1_8_0_2 _  __ Oreans Technologies"
	strings:
		$a = {B800000000600BC07468E8000000005805??0000008038E975??61EB??DB2D????????FFFFFFFFFFFFFFFF3D40E800000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
