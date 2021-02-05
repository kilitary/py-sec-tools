rule _Themida__Oreans_Technologies_2004_duekbl
{
	meta:
		description = "Themida __ Oreans Technologies 2004"
	strings:
		$a = {B800000000600BC07458E8000000005805430000008038E9750361EB35E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
