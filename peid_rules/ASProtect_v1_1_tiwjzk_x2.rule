rule _ASProtect_v1_1_tiwjzk
{
	meta:
		description = "ASProtect v1_1"
	strings:
		$a = {9060E81B??????E9FC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
