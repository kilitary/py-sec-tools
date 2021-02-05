rule _ASProtect_v1_1_MTEb_sqrygw
{
	meta:
		description = "ASProtect v1_1 MTEb"
	strings:
		$a = {9060E9??04}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
