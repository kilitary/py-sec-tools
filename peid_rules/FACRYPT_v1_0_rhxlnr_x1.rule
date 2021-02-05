rule _FACRYPT_v1_0_rhxlnr
{
	meta:
		description = "FACRYPT v1_0"
	strings:
		$a = {B9????B3??33D2BE????8BFEAC32C3AA494332E403D0E3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
