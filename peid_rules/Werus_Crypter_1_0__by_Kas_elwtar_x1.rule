rule _Werus_Crypter_1_0__by_Kas_elwtar
{
	meta:
		description = "Werus Crypter 1_0 _ by Kas"
	strings:
		$a = {BBE8124000803305E97DFFFFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
