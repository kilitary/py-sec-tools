rule _ILUCRYPT_v4_015_exe_lpsnsq
{
	meta:
		description = "ILUCRYPT v4_015 _exe"
	strings:
		$a = {8BECFAC746F7????4281FA????75F9FF66F7}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
