rule _ThemidaWinLicense_V1_8_X_V1_9_X__Oreans_Technologies_vpeyes
{
	meta:
		description = "ThemidaWinLicense V1_8_X_V1_9_X __ Oreans Technologies"
	strings:
		$a = {B8????????600BC07468E8000000005805530000008038E9751361EB45DB2D????????FFFFFFFFFFFFFFFF3D????????0000582500F0FFFF33FF66BB????6683????66391875120FB7503C03D0BB????????83C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
