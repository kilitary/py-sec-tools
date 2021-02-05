rule _E2C_by_DoP_yqvzix
{
	meta:
		description = "E2C by DoP"
	strings:
		$a = {BE????BF????B9????FC57F3A5C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
