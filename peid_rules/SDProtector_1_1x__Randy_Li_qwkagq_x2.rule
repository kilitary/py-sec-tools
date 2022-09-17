rule _SDProtector_1_1x__Randy_Li_qwkagq
{
	meta:
		description = "SDProtector 1_1x __ Randy Li"
	strings:
		$a = {558BEC6AFF68????????688888880864A10000000050648925000000005864A300000000585858588BE8??????????????000000????????000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
