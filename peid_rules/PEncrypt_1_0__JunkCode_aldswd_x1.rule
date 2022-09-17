rule _PEncrypt_1_0__JunkCode_aldswd
{
	meta:
		description = "PEncrypt 1_0 __ JunkCode"
	strings:
		$a = {609CBE001040008BFEB9????????BB78563412AD33C3ABE2FA9D61E9??????FF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
