rule _codeCrypter_0_31_gkraza
{
	meta:
		description = "codeCrypter 0_31"
	strings:
		$a = {5058535B90BB????4000FFE390CCCCCC558BEC5DC3CCCCCCCCCCCCCCCCCCCCCC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
