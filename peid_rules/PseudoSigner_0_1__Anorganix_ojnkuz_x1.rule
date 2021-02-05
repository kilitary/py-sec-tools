rule _PseudoSigner_0_1__Anorganix_ojnkuz
{
	meta:
		description = "PseudoSigner 0_1 __ Anorganix"
	strings:
		$a = {558BECB9040000006A006A004975F95153????????10E82DF3FFFF33C05568E831001064FF306489208D45E0E853F5FFFF8B45E08D55E4E830F6FFFF8B45E48D55E8E8A9F4FFFF8B45E88D55ECE8EEF7FFFF8B55EC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
