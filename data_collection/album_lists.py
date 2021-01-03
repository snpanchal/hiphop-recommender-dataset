# these albums have a 0.4 < liveness < 0.5 and are live
albums_to_remove = ['6HSnVwIMF1WIat7Zo5nlEk', '5zbuWnugNgJr4Jk4zpmhid',
                    '74hPuIcd2Wa0T3FRqtTKHX', '7ctCScnWG0nMedlfUiauOk', '6bmqTZoqZg43Q6Ir9KxuJX']

# these albums have liveness >= 0.5 and are NOT live
albums_to_keep = ['0H75KrMC04ITghNn57ilyE', '2PpxxoArVS7VEVhZlSOhY1', '6CDkzOkrL9Xd8tSy3IEzpB', '1PIRK8f52VBEEYjuSi4YMQ', '2NwBTEDVO8Kt4FUvyU0lhY', '08bWP7UxqYWNzGR7bWNyUz', '1vlcxiPI1nVfyTak4mncGk', '61OEfavu9kM9nHTdbPPH3H',
                  '2JW8rnVDxP2jGHb3Clo6Au', '1GVfIlaZgK28laAqe8oFEu', '4VKQkZAaF9XLj9ZOVcrfN3', '776ihjJKcK7Y75dZqNEf6S', '3LBapZleXFpxvcLx0S7MWj', '3LBapZleXFpxvcLx0S7MWj', '0fq11sFx5SoPzaX7Lh9CFJ', '5z8Esh0TPpFjw0IqzItBAt']

deluxe_albums = ['7xUgIBz1WYKyXj8Fj5EKCv', '7oc6i8xUILaWwQ5BJMZS3c', '7kuxxSvj3RxPjqFBHuX68w', '7kgdhIdRUXU7gcCmLANQQK', '7eJt0QB6bN6JiqoBTVO7KS', '7aXpfvnCNztfsn1erE1Eaj', '7HWRfeoyrAKJgsufGbgxkc', '7GmwwE2wcNtyq7nlsrYVuD', '7Et3bSTLLqdABO1qCxUplS', '7DyAbrlPQTi2v6DAmgC8Qa', '7AUsm4Nzd6ApSgkLCHSjia', '7A28UW6Soot4jfbWYol4Zc', '71R6Zql0xbWd4YDNkXSVU1', '6zA5X3CQ5rgLKhTobyV5Id', '6wmcBak0mxYsK5F9adUrVT', '6wRev1uYL0JsMsWqktJuVi', '6rzMufuu8sLkIizM4q9c7J', '6jiB86M8iPw4XBo0s6Fu4V', '6guJZpZ52v4MrJKIH7tASl', '6fABwONLawdFjkDpLx41j8', '6eGYLONkDMja0MNtZWnRRB', '6b7NVGKHlwKyQzFKoVTaMA', '6YlDIxqEjvY63ffH6AwCjd', '6X1x82kppWZmDzlXXK3y3q', '6WG1LSZbJCwtGIuaGB0UUi', '6VML3yX1WR5pXtg6fmwdzZ', '6SmnTJAiNEoIsoysDN2dxY', '6SL49HqoUwu2hhfukBAK3Q', '6Pqlfg42Sc3ElNuyt5NUiK', '6JMWAgn3qLyNrv153nclRq', '6HXlnhMr40FP2qBTnKXRbA', '6FfYIKA59pCFs2d1FB79Pq', '6DxSrvqVwXO3SmFDSGuLAi', '6DN7GcZF1HywzrkGN6Eeqk', '6Ajq0fVuPxZ8igxZfvad7f', '6ACieouaVnMczR5pwEJqRz', '60QP93G98tBVQnB6qWROtY', '5ztTCKLCKuiIXzXpbqdUGa', '5xtAAHr59ozJ2PQ67utEmi', '5xYelOucTX5yIB93L6CVo4', '5uA3r5ucAXyJgn3iWCWIJb', '5smHQ1uTrerU8DyRaqTyxh', '5s0rmjP8XOPhP6HhqOhuyC', '5rJDj8p6MqWx41Evt63gtK', '5qs8T6ZHSrnllnOuUk6muC', '5pYJCnVKIXdZVySWQe4DEl', '5pL6fzBD4sLs9hyau2CeUi', '5ooCuPIk58IwSo6DRr1JCu', '5hLzlv5DYQSSPElh9ZIKr8', '5fwdtSABKLaSOMT3UhpWa7', '5dwoMolw6tiaf3wiFITBRG', '5dROr3bb551hRGk7cTiS8A', '5abCMGtyHwpOr9cEbwfP1P', '5ZIAAbPTKcVEL0MzPT4aYP', '5X7YemhrtWCDbskmoMQSLt', '5TxNe8YWfuK5FhDUVnGIlp', '5Sskfr26AzgFTIeEYrQ4CP', '5S4SuPHbaozi5PDedAONTG', '5S39sWIHkhd8jxdUelQxXF', '5PKYeoSKEVQd7ZTnwnWRn7', '5OQ46UiKltoHtHrGFXB1HI', '5NzdnPboXcqvuvyEH1wSEJ', '5NTOvCGu7HT4DgJGLXtKUU', '5NADcYAHh2rgbABVsXhaiv', '5KOQHt4JKmtDbC4k1YLuBl', '5Hsaxc6a2GWPAqXttPFbY0', '5Hs43ta4vAYKRRRR7DKjt9', '5GAvwptqr4r63i8lZWrL58', '5FP9keIJnlSCKnkdVOf623', '5ECtjGOFXwDA8nVhBARKv6', '55yej6pFoAi29Qs4VjNpB0', '54s3m8cL3z0fMc5ZWlrrvt', '52et8iMqxot7nq4L7jY2t9', '51HDsvvActcDmYy7NQl6oL', '4yE6WFFun0KjJXbdWkoVrp', '4v0IxMbMN975IfxFHzgK9d', '4pCLvRkipIlKyngrIdk4ec', '4ljsev5vUnwB2BUFAMvwwy', '4kdtsPVTldsCerugQPQG9w', '4kO7EI4XxT5M0BMkrx0mBh', '4iXkOqmH7192V5Hc7EDwMw', '4Y8PzZe0BZMp6XtZ3Lj3mD', '4Wz9OY9vLIGHlTXtlanwio', '4TzJROIsnfOkLUWmeOjt2F', '4TdiCmBKujkiyMeJ1guJJa', '4Nlbt2EuXedr6UqaeXEI4c', '4Maqwoh2mr48wdCPUevRIM', '4GvDHEW1goHkqJbLJHzUUf', '4FMyltvm5TbU3v2wsmWdao', '4FADvCXok2GhepAWLE8Fs1', '4E1KSgWQUNHADgur2Rwr58', '4DP4IfbpAvbm9HyPnSboiX', '4C1DuH3NaQQSOFTjmjagv5', '4B4V2xsaNdlRE2BaVb1w24', '49zB39sak50ghwZMwHQqQ0', '49qpwRDGLfNAkUG9UeGoTV', '49FwsZq64UotAHB0CXGR1N', '44jrX3SThj7pFjOzUTLm85', '42wO2hmYMe3tQGMoshwFsI', '41z6xTqpuX5Y06vaPiWh0U', '40XGTQ7FN6Y3dZXJhKBe96', '40VtQmfgdaVmh95sjosyQq', '3z1SIQxDVrzNgI2Xgjph6H', '3wPd5PnHMlkeRCabXyX57s', '3wOMqxNHgkga91RBC7BaZU', '3vyMhFtK8R0cFoMfnBfztb', '3sDoSYf2AKB2IegZmkISGD', '3raeLaYMyhfb67HgnnNrsg', '3quLLvWeivpGuxi3WiGgzg', '3ppiimGI1l1CXb5XjtORrR', '3nVqeuOMLIkIgIltdgVD6I', '3dWcsI32Xb5dEYfYgzSFtk',
                 '3dO7PSIElcpvMtHUqREVrp', '3aITAVBURujVe8fhI2seeR', '3WUe1HRgE7qoUQ3oejofGf', '3T02fCxAjApu18taJLLbyN', '3SsqQj9XJMCJplYeCtMill', '3Sem4xOyBVenGDNyZMp00V', '3PxXiYU3PjymOEE22PewGZ', '3PkWTXolCR9RkJrKiAsf55', '3NyOgmRtkGJWCa3MfTGH5L', '3N9kar9VT6yLh3cqPEwlbS', '3JuFDAPIook5dzr7KKGAzn', '3IO8IPjwXuzPJnoaqkwYrj', '3DgcU1Rvkf4giCPlNbHcRg', '3DPaxBsMtMsO4RAbA18yUG', '3Ba5eDpzB4yLBfJsraQM4G', '39cYf3pTMlhpCYNpggKE2I', '39FNg2ShzXn1VFUiqY6IWe', '38tSxbJgFfV68aOzRGW1X6', '36QdZp3YRchiFzffEyu5YL', '35obNd6fbY65iCgIOSkyN7', '35KyVKa5AMTaOBxSzjSBbK', '31lHUoHC3P6BRFzKYLyRJO', '315T9HtENm6sUXEE7vhgjS', '2ydmGsz8W6qDq2UgotdxzR', '2wtx5XeYMFOpY40eK9f7fA', '2tl87d3qbkmxSw5J5YEQUI', '2pl9PVgr8QFKRGY0HY69GI', '2owsJCZ8OoEkNbfBp1My4r', '2ljUSR5STBQGeiqjrfWbSe', '2lTzPbjHdZgNyV5cvhT7qE', '2kx4l1OQNT2JXLld9HJDIh', '2kSTssn90EgrYWNlWZJ9r4', '2gKQvajkEEaDtkqJ8FJ4uw', '2gBoDoKdOGMv3OephKw2B0', '2f8GNcpOMomZdJ4EkEGs1E', '2dnvkiEsLtEMOAmM0DaZVo', '2dCTTPgK1MdIFe5ozsppxU', '2c6s84YTwR9cfncPmB9fNW', '2ZUFSbIkmFkGag000RWOpA', '2S8AWAM0nxyFy66YnUfIs3', '2OWLbSd0bRFLw2M0KlgrgJ', '2MDU46hcBn3u94s46BOSdv', '2KlVwY7H9B9KvFXJglqzWq', '2J66oEpWvvNIh0QC3GCmjy', '2G3PKovGjfQwTaH74HNj75', '2D2rriWruRrRFq2AAholPp', '2Af2xpOLk0VzzJqmqtAW8T', '28WQaaytjIifjWwDHS6bfv', '26BjZp8Bqknb0FU0ND1oLG', '24wBNDuNst0P8J6FXmKa3U', '24jAbLMFzCTlIv3kQ94HwK', '24IexOT10jPuK3MR6cS3ag', '22py1IeIi51c0GBYEHQTsI', '1yw6pIVYjbf9WoLiPkIPJv', '1yCnOPMq0BVzKKn97HiIFp', '1y94GzWaVGqSbMSxzaFEFQ', '1wBFRaacNYmqfkidUZ0NtM', '1r8dmj9V9ccKNlnLEtFuIH', '1qXoQyLW6uBNVLsC4jleZC', '1oDgCslpzVA6zATNLPFo7f', '1kTlYbs28MXw7hwO0NLYif', '1gUI4keDXbeSil6rwY9qUm', '1esJd1JGPa7jDRAKrYs6ls', '1ePa4Xo4oDjldGmhwT4SfK', '1dkvQiAwd1ONpvxAHzLPKl', '1dDfjR6KqXwa6I8XmPXnxr', '1ctEzpKcYukYAOXpyXx7C9', '1beC92PkyCuvr8gOUeR0wW', '1aMPeVSgyoG34dAu7iwRpD', '1YwzJz7CrV9fd9Qeb6oo1d', '1YZ3k65Mqw3G8FzYlW1mmp', '1YSb516nyR6ALY2ji1eCAV', '1RWgm4YvRL0YN1iX1Mto7b', '1OD8C2DoR0Lf4FcnFZo36K', '1MzE8KeSTNbs3iNosDI7d3', '1MeObtDxA5hKKICWaOHzxK', '1I7F1oBXY4pb007rHyagDz', '1CYcnRiV2J9bWGCXbXrvQC', '19DGkH750PrQMMnKqBAxfY', '167TDd2jTmMgTkB8thzyI9', '15QCrOnubJ2AiL43z7stt0', '14hX4TVbfWbJdHMSvRZW69', '13lMLnHs5qsmm687oRc3VC', '10jogO732o8oGvsjVpWRmO', '0zicd2mBV8HTzSubByj4vP', '0zhZDmHEtDtok393SbZ3d7', '0ymZEUngBCetAJcJaqO63b', '0woceOIRsWm2ZOk2ZZ9v5W', '0vCz96STComPDw5SOC8RHn', '0s9cSoniuN0HfXpwlCpGUF', '0l53NPQef4eLh7UDcG9gtJ', '0kM9NWP6oR8u9GCfbOzvtD', '0kEgU7XiRXcJ7TptKepwxC', '0jzmYAItbZraWCe16ODaWW', '0fUy6IdLHDpGNwavIlhEsl', '0fEO7g2c5onkaXsybEtuD2', '0etTihuf1RPKLobUzPhGaa', '0a6nvQQ7hqmFbqAZVUanDW', '0Xw0t4mxvxwOKo82dRd89k', '0WBW3ce6leISM9TYlt0l4d', '0VWYRbEcvJcPrqMGJirO6q', '0V68iflWNZri1Zc8txsLyg', '0SHeOTuKXo4cM1CWyAwDcj', '0RYhvwOBxLMkiLYSCVSUXK', '0P4u1ZRM6CXePgpeF8ShmN', '0NvirtaDCaZU5PAW1O5FDE', '0D2kFxAO1YPAuxAtP23g0p', '0CoiTAUBiO70lic9p9Lboq', '0Ab4fSWyGsgCxqZauCGfa5', '05gKNAgBzLOGmTNVsGtP6p', '05Qg48LlYGKYdeXrNGg00g', '03L5vIoDkCn0STNBAwTDEF', '00kSgH9g6nYBQhjnRQFBew',
                 '2YRztyAcEZqMA6UjcrG2vk', '2CrhjdQvzrbNA5LwyDVbro', '2G5p3c3YO8l63QfGKSxzBx', '2CrhjdQvzrbNA5LwyDVbro', '6hrwAx3KoigDlYJx2TCAwC', '1i4Ju3OL0Tq6QaAO2OUVdE', '2UhsaD0bC85zPZEWjshoJf', '4zK2YeF922VXfzyxFteIfT', '3tQd5mwBtVyxCoEo4htGAV', '59Ti0MtssgtVxrVE6T7oyR', '1ucCcn3bSPePeI67kUapwB', '5c4JW9TBpawiv9pI2vrNsE', '4SVTdeKqXEcmURWj9KCWR4', '6GRMwGaxdugCdDN3TtoHZz', '5opAMGIf8Hn7xIaTPdHFDv', '53haOw4fOh1rNZK8xKgGY8', '57FQTvThrTFPrGPAvZCjw6', '5nK0vU32lSmcGrglfcOfg8', '1oQef7548sivCtMQwK8Wgo', '18XFe4CPBgVezXkxZP6rTb', '7sHrPadM39466NY7DW3s4r', '10nO3EJJDMm6j6d2uK3Jah', '3Fa7c5eB1TiAhoyhS4ReNi', '0gOjpREhEh5WEBNqz5Fzkw', '3Y5gM9xG4U5bXyMjpPWIRP', '6qBNm8dkdowRUUrN7uwR11', '0vRpQxm2gAiDXn7Tv0eT83', '3vegD41O8gRipwd6NpDFt6', '1O7DRoZBdEUGqm1KkJL4OC', '6t5g3iBwXlDWXhSZbDonrJ', '46tIBaFs0Ov0HJsCDrq1Kl', '0L1Qq8en6hODRCgaAfTBAq', '0gaLZATMEssSErDzywUqxD', '5rWTCXmYHC6Zr8uZAGF9Cg', '0idU1VT6ONFjprwVvNYs8N', '2YRztyAcEZqMA6UjcrG2vk', '3173F5zjUTsRypoGS9NpKx', '6knhloHm0j18ADzlJj3Xvb', '4O0zNlIF1azFpzDB6NsYVc', '52D2v3pzp70PRdjH2HDKO0', '4Mk0h5wMrYNvOefZXi7Jke', '0cNg3qCbZ047iZ6kwK1nPN', '51pWPRmyRyrh4GDwUjWmkM', '5A2KhChS9TkI0uK6FXqeFv', '0RoKDOUkZZN61ddvyuIl2P']

commentary_albums = ['5us9KdofiGcesaP6FLa9CM', '3dP0TFEEzTXJQKtrpsKFUj', '6Unh7vKoCUagA0oGtg53q0', '6IwOfFHgToNNwPONpcYsac', '1bA2nEUbbwmW81BWYy1DPS', '6nRmgnXFlSsfPYTtRp52gR', '6lH6sJtPXSHNVXGx0s1sIr',
                     '26JLBgmg9yNxBcdBhX0f63', '34Vqb2m74NU6Pb682ymHic', '0LKBtML04xZwUb30hCTopp', '69C7wlBDl96476XcRmsPc6', '0XUNsey9tSBuKPt1aS9M7l', '0FnTw6TY6iB5AHATPzCYkd', '4WNXpeZR1jc2NFgOAeyLMB', '2EvIPfiWOIxIZ193E8sK8w']

instrumental_albums = ['1GYG80diXFWYwH7FJB7KeC', '6OqspD61fsOYzSjXNDb0od', '2MalAcbGXGJaeYchXjkndA', '0ic6rMSwqDasuXSA7zJ1pw', '3iJ6a4ZkifqzLRgClVsemH', '3k2ZKHGhbrrlU7PVVTlRr0', '6spi3faBh90zAqXiz9f7FZ', '2oZJWv0aUh4vn9jelnH4ld', '3LYvDGtOCYE9sAXUVZ9elI', '4v0sRArgHmBWfTnJr2EpMG', '0tuVCtw7vxMAaYNA56ejQC', '3t3Ar2cJUVLY6yTRmrezI8', '6LkUDxtz8cJG3n0RbZNkDh', '0z0rbyEtYkisRJBja0FmRk', '10O7EUPKcnHr83uLZ05B04', '5WXpW898b9Fd7GmRrrtMcu', '6YxjD9sRNGNOGGXuFzI5pF', '0hWXtK4mP6Be6AHIllknU7', '2bgsETml3VW32hNj7cVsoA', '6ZG30WjlBXKaPjllfRhAqp', '4VTvPRZN3YUjdIVWEF2Jxy', '53pQychJ4jQA3viH42pI90', '6c58lk5hGk9TuZiSXIXEn8', '0Uc46FMjlmZCgceWO2Zwkj', '0PLEQ4a31O4cOHFFlAtJ53', '5obiyJomz6ypITdwLIdNkv', '7GvdgeSyGWQ8x7RrchZkU3', '3GTqCedna2bhn0VFmis3Ok', '038gDvDZUgNGEpJajpP2pm', '1w078GmybN2wcVTqC63G6Y', '3QszZDoHrIhFQlBOEO0ltD', '6vN44bEuASeEHiPXCoIjpU', '57S0fnVIa7OgwbMbNF4gmi', '3516eqz7b2Bfid6LoWxO4Z', '06Ee6dveq170ls1t52Cj6s',
                       '4WklNeLYQAuEOV83vL7hcO', '742JlWjVoujLG7tS2s4pZN', '0MVVp47QW8V5o4wI5VowJV', '4QCReojarEyY8twLScsDPO', '6QLa28h4nnQTH3Wc43ozyq', '3qBjWOPsBWKPlVlclxIeWZ', '4ZgoUMko1TbkyytjaDHrAe', '54Dg6crsJSj1SM8nvhI9wz', '5gfRd564uUnlGBEL7U6gc7', '1KdkiRofNjI5sNWEmtwOx3', '2L32VPdX8NcICxVf6AhDqD', '17ZhcHozi6jHtSmMxDk1R1', '5V3Chnpno9oTI7JSPXKUf3', '5s8SR0lxHs1ZqzuSDfXtM7', '2Dp2JalIuXdPsu9GWhTZGl', '6Yv7iXDdfj8WNXkMR2rtHj', '1NPoeFSdrx5vVW2SambpCG', '2opbjR8Znpj0rKMDfbd8JR', '7nmtzsgs0G7CHaEZO1qdnn', '0baxtwETSL9uVjKBb6e4qw', '2LHeqwR8oNodZWwuoVjorx', '71R6Zql0xbWd4YDNkXSVU1', '3s5S4XAC5HgHaTyH5Nm8ED', '55bxY6BzDiNcmAcp7A3ZUv', '1rbggSZPdqgiR1UGMyzRRx', '3lXpgWLPercbWXQ3bRKuhg', '2EejRWDjKI2hruzpTykT5d', '4a6u9TUkH1MW2zZkFUYlV0', '7gdfgCWRXLD9AYiWkz0zJB', '7LB3xpvIUesIeCPl0iOQXS', '5AW4FwzZSKW1se5qWQCrR1', '4NXeGThanoN7UT5kvwEyxS', '4MIvq6fbE7UtIRTc2mB2pw', '4BE9dkZuaLvZgbRlQ5DGlU', '1zuAuY8CdOjVIN1kKimFgS', '1gvkFTPF1rKpNnbfzitx5T', '4xW2BxaorYk4ejt78KJUVk']
