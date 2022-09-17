rule _PEnguinCrypt_v1_0_stabgo
{
	meta:
		description = "PEnguinCrypt v1_0"
	strings:
		$a = {B88CD3153375813EE80F009AE8F9FF9A9CEB019A5980CD01519DEB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
