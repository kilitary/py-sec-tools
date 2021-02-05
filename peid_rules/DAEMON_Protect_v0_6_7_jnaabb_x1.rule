rule _DAEMON_Protect_v0_6_7_jnaabb
{
	meta:
		description = "DAEMON Protect v0_6_7"
	strings:
		$a = {60609C8CC932C9E30C520F014C24FE5A83C20C8B1A9D61}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
