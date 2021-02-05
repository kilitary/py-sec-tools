rule _PKLITE32_v1_1_qomtjl
{
	meta:
		description = "PKLITE32 v1_1"
	strings:
		$a = {558BECA1????????85C07409B801??????5DC20C??8B450C5756538B5D10}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
