rule _ASProtect_v1_1_MTEc_xdntbp
{
	meta:
		description = "ASProtect v1_1 MTEc"
	strings:
		$a = {33C0BE????8BD8B9????BF????BA????474A74}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
