rule _PE_Lock_NT_v2_01_kauolf
{
	meta:
		description = "PE Lock NT v2_01"
	strings:
		$a = {EB03CD20C71EEB03CD20EA9CEB02EB01EB01EB60}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
